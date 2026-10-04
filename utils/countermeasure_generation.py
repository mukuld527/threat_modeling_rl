from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter

'''
Considering the STRIDE threat modeling framework, all OWASP Top 10s, all NIST frameworks, and all other available applicable frameworks, 
Generate a CSV file containing threat modeling countermeasure titles and their corresponding description and remediation solutions. 
Based on the number of components any desktop or mobile application is using and different hosting platforms
'''

wb=Workbook()
ws=wb.active
ws.title='Threat_Countermeasures'
headers=['Framework','Category','Threat/Countermeasure Title','Description','Remediation Solution','Applicable Components','Hosting Platforms']
for c,h in enumerate(headers,1):
    cell=ws.cell(1,c,h)
    cell.font=Font(bold=True,color='FFFFFF')
    cell.fill=PatternFill('solid', fgColor='1F4E78')
rows=[]
entries=[
('STRIDE','Spoofing','Strong Authentication','Prevent identity impersonation.','MFA, FIDO2, OAuth2/OIDC, certificate-based auth','User Auth, APIs, Mobile/Desktop Clients','On-prem, Azure, AWS, GCP'),
('STRIDE','Tampering','Integrity Protection','Protect data and binaries from modification.','Code signing, checksums, secure boot, TLS','Applications, APIs, Databases','All'),
('STRIDE','Repudiation','Non-Repudiation Logging','Ensure actions are traceable.','Centralized logs, immutable audit trails','Apps, Services, Admin Portals','All'),
('STRIDE','Information Disclosure','Data Protection','Prevent unauthorized data exposure.','Encryption at rest/in transit, data masking','Databases, Storage, APIs','All'),
('STRIDE','Denial of Service','Availability Controls','Reduce service disruption risk.','Rate limiting, WAF, autoscaling, caching','APIs, Web Apps','Cloud/Hybrid'),
('STRIDE','Elevation of Privilege','Least Privilege','Prevent unauthorized privilege gain.','RBAC, PAM, segmentation','OS, Apps, IAM','All'),
('OWASP Top 10','A01 Broken Access Control','Authorization Enforcement','Restrict resource access appropriately.','RBAC/ABAC, server-side validation','APIs, Web/Mobile Apps','All'),
('OWASP Top 10','A02 Cryptographic Failures','Encryption Standards','Protect sensitive data.','AES-256, TLS 1.2+, key management','Apps, Data Stores','All'),
('OWASP Top 10','A03 Injection','Input Validation','Prevent code/query injection.','Parameterized queries, sanitization','APIs, Databases','All'),
('OWASP Top 10','A04 Insecure Design','Secure Architecture Review','Reduce design weaknesses.','Threat modeling, security architecture reviews','All Components','All'),
('OWASP Top 10','A05 Security Misconfiguration','Hardened Configuration','Remove insecure defaults.','Baseline hardening, CIS benchmarks','Servers, Containers','All'),
('OWASP Top 10','A06 Vulnerable Components','Dependency Management','Reduce third-party risks.','SCA scanning, patch management','Libraries, Containers','All'),
('OWASP Top 10','A07 Authentication Failures','Identity Security','Strengthen authentication.','MFA, lockout, passwordless','Auth Services','All'),
('OWASP Top 10','A08 Software/Data Integrity','Secure Supply Chain','Protect software integrity.','Signed builds, SBOM, CI/CD controls','Pipelines, Packages','All'),
('OWASP Top 10','A09 Logging Failures','Monitoring and Alerting','Enable detection and response.','SIEM, audit logging','Apps, Infrastructure','All'),
('OWASP Top 10','A10 SSRF','Outbound Request Controls','Prevent unauthorized server requests.','Network allowlists, metadata protection','Servers, APIs','Cloud'),
('NIST CSF','Identify','Asset Inventory','Maintain asset visibility.','CMDB, automated discovery','Endpoints, Servers, Apps','All'),
('NIST CSF','Protect','Access Control Program','Protect organizational assets.','IAM, conditional access','Users, Systems','All'),
('NIST CSF','Detect','Security Monitoring','Detect anomalies.','SIEM, EDR, UEBA','Endpoints, Servers','All'),
('NIST CSF','Respond','Incident Response','Contain and remediate incidents.','IR plans, playbooks','Organization-wide','All'),
('NIST CSF','Recover','Business Continuity','Restore operations quickly.','Backups, DR testing','Critical Systems','All'),
('NIST 800-53','AC','Account Management','Control account lifecycle.','Provisioning/deprovisioning','IAM','All'),
('NIST 800-53','AU','Audit Events','Record security-relevant actions.','Centralized logging','All Components','All'),
('NIST 800-53','SC','System Communication Protection','Protect communications.','TLS, segmentation, VPN','Networks, APIs','All'),
('NIST 800-53','SI','System Integrity','Detect integrity issues.','EDR, anti-malware, FIM','Endpoints, Servers','All'),
('Mobile Security','Platform','Secure Local Storage','Protect device data.','Keychain/Keystore, encrypted storage','Mobile Apps','iOS/Android'),
('Mobile Security','Runtime','Root/Jailbreak Detection','Identify compromised devices.','Runtime checks, attestation','Mobile Apps','iOS/Android'),
('Desktop Security','Endpoint','Application Whitelisting','Run only approved software.','WDAC/AppLocker policies','Desktop Apps','Windows/macOS/Linux'),
('API Security','API','API Gateway Controls','Secure API exposure.','AuthN/AuthZ, throttling, schema validation','APIs','All'),
('Cloud Security','Infrastructure','Cloud Posture Management','Reduce cloud misconfigurations.','CSPM, guardrails','Cloud Resources','Azure/AWS/GCP'),
('Container Security','Container','Image Hardening','Reduce container attack surface.','Minimal images, image scanning','Containers','Kubernetes/Cloud'),
('DevSecOps','Pipeline','CI/CD Security','Secure build and deployment pipelines.','Secrets management, signed artifacts','Build Systems','All'),
('Zero Trust','Architecture','Continuous Verification','Never trust, always verify.','Conditional access, segmentation','Users, Devices, Apps','All'),
('Privacy','Compliance','Data Minimization','Reduce privacy risk.','Retention and classification policies','Data Stores','All'),
('Network Security','Network','Segmentation','Limit lateral movement.','Microsegmentation, firewalls','Networks','All')]
for r in entries: rows.append(r)
for i,row in enumerate(rows,2):
    for j,val in enumerate(row,1): ws.cell(i,j,val)
for col in ws.columns:
    ws.column_dimensions[get_column_letter(col[0].column)].width=min(max(len(str(col[0].value))+5,20),45)
end=ws.max_row
ws.add_table(Table(displayName='ThreatCatalog', ref=f'A1:G{end}'))
ws2=wb.create_sheet('Component_Guidance')
ws2.append(['Component Count Range','Recommended Activities'])
for h in ws2[1]:
    h.font=Font(bold=True,color='FFFFFF'); h.fill=PatternFill('solid', fgColor='38761D')
for r in [
('1-5','Basic STRIDE, OWASP Top 10 review, SAST, dependency scanning'),
('6-20','Add DFD threat modeling, security architecture reviews, IAM reviews'),
('21-50','Add automated threat libraries, cloud posture management, red-team exercises'),
('50+','Enterprise threat modeling program, attack path analysis, continuous validation')]: ws2.append(r)
path='/mnt/data/Threat_Modeling_Countermeasure_Library.xlsx'
wb.save(path)
print(path)
