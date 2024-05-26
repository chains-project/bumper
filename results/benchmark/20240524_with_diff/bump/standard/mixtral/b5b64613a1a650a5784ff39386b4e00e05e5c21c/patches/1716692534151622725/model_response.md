```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl() != null ? server.getUrl() : "", server.getArtifactory() != null ? server.getArtifactory().getUrl() : "", server.getDistribution() != null ? server.getDistribution().getUrl() : "", step.url != null ? step.url : "", step.artifactoryUrl != null ? step.artifactoryUrl : "", step.distributionUrl != null ? step.distributionUrl : "")) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (org.apache.commons.lang3.StringUtils.isNotBlank(step.credentialsId)) {
        if (org.apache.jenkins.plugins.p4.util.OkHttpUtil.isNotBlank(step.username)) { // Replace deprecated Apache Commons Lang with OKHttpUtil
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (org.apache.jenkins.plugins.p4.util.OkHttpUtil.isNotBlank(step.password)) { // Replace deprecated Apache Commons Lang with OKHttpUtil
            throw new java.io.IOException("'rtServer' step can'sk include both credentialsId and password");
        }
    }
}

public final class OkHttpUtil {
    public static boolean isNotBlank(String string) {
        return org.apache.commons.lang3.StringUtils.isNotBlank(string);
    }
}
```