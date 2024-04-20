Here's the patched version of the failing method:

```java
@java.lang.Override
protected org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance run() throws java.lang.Exception {
    if (org.apache.commons.lang3.StringUtils.isBlank(step.url) && org.apache.commons.lang3.StringUtils.isBlank(step.artifactoryUrl) && org.apache.commons.lang3.StringUtils.isBlank(step.distributionUrl)) {
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

The patch replaces the `isAllBlank` method call with `isBlank` method calls for each argument. The issue was caused by the removal of the `isAllBlank` method in the updated dependency.