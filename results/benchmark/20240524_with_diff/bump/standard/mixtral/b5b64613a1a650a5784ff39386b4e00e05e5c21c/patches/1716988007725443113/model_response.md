Here's the fixed version of the method using `org.apache.commons.lang3.StringUtils.isEmpty(CharSequence)` instead of `org.apache.commons.lang3.StringUtils.isAllBlank(String, String, String)`:

```java
@java.lang.Override
protected org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance run() throws java.lang.Exception {
    if (org.apache.commons.lang3.StringUtils.isEmpty(step.url) && org.apache.commons.lang3.StringUtils.isEmpty(step.artifactoryUrl) && org.apache.commons.lang3.StringUtils.isEmpty(step.distributionUrl)) {
        throw new java.lang.IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    java.lang.String urlWithoutSlash = org.apache.commons.lang3.StringUtils.removeEnd(step.url, "/");
    java.lang.String artifactoryUrl = org.apache.commons.lang3.StringUtils.defaultIfBlank(step.artifactoryUrl, (urlWithoutSlash + "/") + "artifactory");
    java.lang.String distributionUrl = org.apache.commons.lang3.StringUtils.defaultIfBlank(step.distributionUrl, (urlWithoutSlash + "/") + "distribution");
    org.jfrog.hudson.pipeline.common.types.ArtifactoryServer artifactoryServer;
    org.jfrog.hudson.pipeline.common.types.DistributionServer distributionServer;
    if (!org.apache.commons.lang3.StringUtils.isEmpty(step.credentialsId)) {
        artifactoryServer = new org.jfrog.hudson.pipeline.common.types.ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new org.jfrog.hudson.pipeline.common.types.DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new org.jfrog.hudson.pipeline.common.types.ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new org.jfrog.hudson.pipeline.common.types.DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```