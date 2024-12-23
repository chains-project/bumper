```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    JFrogPlatformInstance instance;
    if (!isEmpty(step.credentialsId)) {
        instance = new JFrogPlatformInstance(artifactoryUrl, distributionUrl, step.credentialsId, step.url);
    } else {
        instance = new JFrogPlatformInstance(artifactoryUrl, distributionUrl, step.username, step.password, step.url);
    }
    return instance;
}
```