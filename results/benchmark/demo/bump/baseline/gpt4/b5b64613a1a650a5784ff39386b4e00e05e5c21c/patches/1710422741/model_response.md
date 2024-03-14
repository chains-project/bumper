```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer = new ArtifactoryServer();
    DistributionServer distributionServer = new DistributionServer();
    if (!isEmpty(step.credentialsId)) {
        artifactoryServer.setUrl(artifactoryUrl);
        artifactoryServer.setCredentialsId(step.credentialsId);
        distributionServer.setUrl(distributionUrl);
        distributionServer.setCredentialsId(step.credentialsId);
    } else {
        artifactoryServer.setUrl(artifactoryUrl);
        artifactoryServer.setUsername(step.username);
        artifactoryServer.setPassword(step.password);
        distributionServer.setUrl(distributionUrl);
        distributionServer.setUsername(step.username);
        distributionServer.setPassword(step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```
The error message indicates that a symbol cannot be found. This typically means that a method or variable is being referenced that does not exist. In this case, it is likely that the constructors for `ArtifactoryServer` and `DistributionServer` that take two or three arguments do not exist in the new version of the library. Instead, I have used the no-argument constructor to create the objects and then used setter methods to set the properties. If the setter methods do not exist in the library, they will need to be created in the `ArtifactoryServer` and `DistributionServer` classes.