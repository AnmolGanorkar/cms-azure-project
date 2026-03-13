
# Write-up: Deployment Resource Analysis

## Analyze, Choose, and Justify the Appropriate Resource Option

For deploying the CMS application to Azure, two possible infrastructure options were considered: **Virtual Machine (VM)** and **Azure App Service**. Both services are capable of hosting a Python Flask web application, but they differ significantly in terms of cost, scalability, availability, and operational workflow.

### Virtual Machine

A Virtual Machine provides full control over the operating system and infrastructure. This approach allows developers to install any required software and configure the environment exactly as needed.

**Cost:**  
Running a Virtual Machine typically incurs higher costs because compute resources are billed continuously while the VM is active. Even smaller VM sizes generate charges regardless of whether the application is actively receiving traffic.

**Scalability:**  
Scaling a VM-based deployment requires manual configuration. Additional VMs must be created and managed through load balancing or infrastructure orchestration. This process increases complexity when traffic grows.

**Availability:**  
Ensuring high availability with VMs requires additional configuration such as load balancers, availability sets, or availability zones. These configurations add extra management overhead and potential operational complexity.

**Workflow:**  
Deploying the application on a VM requires setting up the operating system, installing dependencies, configuring web servers (such as Nginx or Apache), managing updates, and applying security patches. While this provides flexibility, it also increases maintenance responsibilities.

---

### Azure App Service

Azure App Service is a Platform-as-a-Service (PaaS) offering designed specifically for hosting web applications.

**Cost:**  
App Service provides several pricing tiers, including a free tier suitable for small projects or development environments. This makes it significantly more cost-efficient compared to continuously running virtual machines.

**Scalability:**  
Azure App Service supports built-in scaling capabilities. The platform allows applications to scale vertically (increasing resources) or horizontally (adding more instances) with minimal configuration.

**Availability:**  
The platform manages infrastructure maintenance, operating system updates, and server reliability automatically. This results in higher availability without requiring manual intervention.

**Workflow:**  
Azure App Service integrates directly with GitHub and other source control platforms. This makes it easy to deploy code changes automatically through continuous deployment pipelines. Developers only need to push updates to their repository, and the service handles the deployment process.

---

## Deployment Decision

After evaluating both options, **Azure App Service was selected as the deployment solution for this project**.

The main reasons for this decision include lower operational cost, simplified deployment workflow, and reduced infrastructure management requirements. App Service eliminates the need to configure and maintain operating systems, networking rules, and security updates manually.

Additionally, the integration with GitHub provides a streamlined deployment workflow where application updates can be deployed automatically after each code change. For a relatively small web application like this CMS platform, the scalability and reliability offered by Azure App Service are more than sufficient.

Overall, App Service provides a faster and more efficient development experience while maintaining strong reliability and performance.

---

## Assess App Changes That Could Change the Decision

Although Azure App Service is the most appropriate solution for the current CMS application, certain application requirements could justify using a Virtual Machine instead.

If the application required extensive customization of the server environment, such as installing specialized system software, configuring low-level networking settings, or running background services that require full OS control, a Virtual Machine could be a better choice.

Additionally, if the application needed specific hardware resources such as GPU support, custom security configurations, or non-standard runtime environments, deploying on a VM would provide the necessary flexibility.

However, for most typical web applications—including this CMS platform—the managed environment provided by Azure App Service offers a more efficient, scalable, and maintainable solution.
