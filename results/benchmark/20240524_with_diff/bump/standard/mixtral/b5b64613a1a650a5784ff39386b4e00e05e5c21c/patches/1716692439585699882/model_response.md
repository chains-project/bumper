Here is a patch that you can apply to the code to fix the error:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl() != null ? server.getUrl() : "", server.getArtifactory() != null ? server.getArtifactory().getUrl() : "", server.getDistribution() != null ? server.getDistribution().getUrl() : "", step.url != null ? step.url : "", step.artifactoryUrl != null ? step.artifactoryUrl : "", step.distributionUrl != null ? step.distributionUrl : "")) {
        throw new java.io.IOException("Server URL is missing");
   
    }
   
    if (org.apache.commons.lang3.StringUtils.isNotBlank(step.credentialsId)) {
        if (org.apache.hudson.util.Secret.isNotBlank(step.username)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
       
        }
        if (org.apache.hudson.util.Secret.isNotBlank(step.password)) {
            throw new java.io.IOException("'rtServer' step can'
```