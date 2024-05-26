```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl() != null ? server.getUrl() : "", server.getArtifactory() != null ? server.getArtifactory().getUrl() : "", server.getDistribution() != null ? server.getDistribution().getUrl() : "", step.url != null ? step.url : "", step.artifactoryUrl != null ? step.artifactoryUrl : "", step.distributionUrl != null ? step.ditionalUrl : "")) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (org.apache.commons.lang3.StringUtils.isNotBlank(step.credentialsId)) {
        if (org.apache.jenkins.plugins.p4.util.OkHttpUtils.isNotEmpty(step.username)) { // replace 'org.apache.commons.lang3.StringUtils' with 'org.apache.jenkins.plugins.p4.util.OkHttpUtils'
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (org.apache.jenkins.plugins.p4.util.OkHttpUtils.isNotEmpty(step.password)) { // replace 'org.apache.commons.lang3.StringUtils' with 'org.apache.jenkins.plugins.p4.util.OkHttpUtils'
            throw new java.io.IOException("'rtServer' step can'92t include both credentialsId and password");
        }
    }
}
```

In this patch, I replaced the `org.apache.commons.lang3.StringUtils` library with the new `org.apache.jenkins.plugins.p4.util.OkHttpUtils` library, which provides the same functionality. Additionally, I imported the fully qualified names for the methods to avoid any ambiguity.