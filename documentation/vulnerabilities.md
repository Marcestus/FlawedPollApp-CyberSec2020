# OWASP TOP 10

## Ready implementations

- 6 - bugmode = true, which means that when going to localhost:8000 (which is not in use) you can see all the sites and maybe find sites where to wander

- 5 - to make this more convenient, the programmer has forgotten to make the voting page @login_required so it is fully available to anyone wandering there

- 2 & 5 - because the admin-page’s password sec. controls are non-existent (commented in mysite-settings) one user is using weak password and has accidentally superuser-access to the admin-page, anyone can bruteforce this with a little bit of luck

- 10 - while testing that the password can be scanned, there are no logging of this happening in the admin page or anywhere else


**Test users and passwords**

- bob – builder

- crusty – clown

- evan – allmighty

all users have access to admin page but unfortunately crusty has superuser-access as well


## 1. Injection

Untrusted data is sent to an interpreter as part of a command or query.
Attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.

**Vulnerable to attack when:**

User-supplied data is not validated, filtered, or sanitized by the application.

**Examples:**
An application uses untrusted data in the construction of the following vulnerable SQL call:
String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";

The attacker modifies the ‘id’ parameter value in their browser to send: ‘1’=’1.

**More on the subject:** [owasp - injection](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection)

## 2. Broken Authentication

Application functions related to authentication and session management are often implemented incorrectly, allowing attackers to compromise passwords, keys, or session tokens.

**Vulnerable to attack when:**

Permits default, weak, or well-known passwords, such as “Password1” or “admin/admin“.

Uses weak or ineffective credential recovery and forgot-password processes, such as “knowledge-based answers”, which cannot be made safe.

Uses plain text, encrypted, or weakly hashed passwords

Exposes Session IDs in the URL

Does not rotate Session IDs after successful login

Does not properly invalidate Session IDs. User sessions or authentication tokens (particularly single sign-on (SSO) tokens) aren’t properly invalidated during logout or a period of inactivity.

**Examples:**

If an application does not implement automated threat or credential stuffing protections, the application can be used as a password oracle to determine if the credentials are valid.

Application session timeouts aren’t set properly. A user uses a public computer to access an application. Instead of selecting “logout” the user simply closes the browser tab and walks away. An attacker uses the same browser an hour later, and the user is still authenticated.

Most authentication attacks occur due to the continued use of passwords as a sole factor. Once considered best practices, password rotation and complexity requirements are viewed as encouraging users to use, and reuse, weak passwords. 

**More on the subject:** [owasp - broken authentication](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication)

## 3. Sensitive Data Exposure (seems too hard to implement)

**More on the subject:** [owasp - sensitivite data exposure](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure)

## 4. XML External Entities (XXE) (seems too hard to implement)

More on the subject: [owasp - xml](https://owasp.org/www-project-top-ten/2017/A4_2017-XML_External_Entities_(XXE))

## 5. Broken Access Control

Restrictions on what authenticated users are allowed to do are often not properly enforced. Attackers can exploit these flaws to access unauthorized functionality and/or data, such as access other users’ accounts, view sensitive files, modify other users’ data, change access rights, etc.

**Vulnerable to attack when:**

Elevation of privilege. Acting as a user without being logged in, or acting as an admin when logged in as a user.

Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user. Accessing API with missing access controls for POST, PUT and DELETE.

**Examples:**

The application uses unverified data in a SQL call that is accessing account information:
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery( );

An attacker simply modifies the ‘acct’ parameter in the browser to send whatever account number they want. If not properly verified, the attacker can access any user’s account.

An attacker simply force browses to target URLs. Admin rights are required for access to the admin page.

If an unauthenticated user can access either page, it’s a flaw. If a non-admin can access the admin page, this is a flaw.

**More on the subject:** [owasp - broken access control]( https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control)

## 6. Security Misconfiguration

This is commonly a result of insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages containing sensitive information. Not only must all operating systems, frameworks, libraries, and applications be securely configured, but they must be patched/upgraded in a timely fashion.

**Vulnerable to attack when:**

Unnecessary features are enabled or installed (e.g. unnecessary ports, services, pages, accounts, or privileges).

Default accounts and their passwords still enabled and unchanged.

Error handling reveals stack traces or other overly informative error messages to users.

**Examples:**

The application server comes with sample applications that are not removed from the production server. These sample applications have known security flaws attackers use to compromise the server. If one of these applications is the admin console, and default accounts weren’t changed the attacker logs in with default passwords and takes over.

The application server’s configuration allows detailed error messages, e.g. stack traces, to be returned to users. This potentially exposes sensitive information or underlying flaws such as component versions that are known to be vulnerable.

**More on the subject:** [owasp - security misconfigurations]( https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration)

## 7. Cross-Site Scripting (XSS)

XSS allows attackers to execute scripts in the victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites.

**Vulnerable to attack when:**

The application or API includes unvalidated and unescaped user input as part of HTML output. A successful attack can allow the attacker to execute arbitrary HTML and JavaScript in the victim’s browser. Typically the user will need to interact with some malicious link that points to an attacker-controlled page, such as malicious watering hole websites, advertisements, or similar.

**Examples:**

The application uses untrusted data in the construction of the following HTML snippet without validation or escaping

This attack causes the victim’s session ID to be sent to the attacker’s website, allowing the attacker to hijack the user’s current session.

Note: Attackers can use XSS to defeat any automated Cross-Site Request Forgery (CSRF) defense the application might employ.

**More on the subject:** [owasp - xss](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS))

## 8. Insecure Deserialization  (seems too hard to implement)

**More on the subject:** [owasp - insecure deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)

## 9. Using Components with Known Vulnerabilities

Components, such as libraries, frameworks, and other software modules, run with the same privileges as the application. If a vulnerable component is exploited, such an attack can facilitate serious data loss or server takeover. Applications and APIs using components with known vulnerabilities may undermine application defenses and enable various attacks and impacts.

**Vulnerable to attack when:**

If software is vulnerable, unsupported, or out of date. This includes the OS, web/application server, database management system (DBMS), applications, APIs and all components, runtime environments, and libraries.

**Examples:**

Components typically run with the same privileges as the application itself, so flaws in any component can result in serious impact. Such flaws can be accidental (e.g. coding error) or intentional (e.g. backdoor in component).

**More on the subject:** [owasp - components with known vulnerabilities](https://owasp.org/www-project-top-ten/2017/A9_2017-Using_Components_with_Known_Vulnerabilities)

## 10. Insufficient Logging & Monitoring (seems too hard to implement)

**More on the subject:** [owasp - insufficient logging & monitoring](https://owasp.org/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring)
