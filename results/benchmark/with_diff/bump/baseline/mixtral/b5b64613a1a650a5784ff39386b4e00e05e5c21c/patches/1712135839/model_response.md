Here's the fixed `run()` method with the error resolved:

```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (StringUtils.isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = urlWithoutSlash(step.url);
    String artifactoryUrl = artifactoryUrl(step.artifactoryUrl, urlWithoutSlash);
    String distributionUrl = distributionUrl(step.distributionUrl, urlWithoutSlash);

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (!StringUtils.isEmpty(step.credentialsId)) {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}

private String urlWithoutSlash(String url) {
    return url == null ? "" : (url.endsWith("/") ? url.substring(0, url.length() - 1) : url);
}

private String artifactoryUrl(String artifactoryUrl, String urlWithoutSlash) {
    return StringUtils.defaultIfBlank(artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
}

private String distributionUrl(String distributionUrl, String urlWithoutSlash) {
    return StringUtils.defaultIfBlank(distributionUrl, urlWithoutSlash + "/" + "distribution");
}
```

The `isAllBlank` method is replaced with `StringUtils.isAllBlank`. I added three utility methods to make the code cleaner. Also, imported `org.apache.commons.lang3.StringUtils` to use these utility methods. Make sure to add the import statement in your code.