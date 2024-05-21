Here's the fixed `run()` method:

```java
@Override
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

I replaced `org.apache.commons.lang3.StringUtils.isAllBlank` with `org.apache.commons.lang3.StringUtils.isEmpty` to fix the compilation error. The `isAllBlank` method was not found, so I changed the condition to check if all three strings are empty using `isEmpty` method.