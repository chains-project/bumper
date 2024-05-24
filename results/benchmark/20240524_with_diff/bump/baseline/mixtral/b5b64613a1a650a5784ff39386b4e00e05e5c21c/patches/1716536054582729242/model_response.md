Here's a fixed version of the `run()` method that should resolve the compilation error:

```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (Strings.isNullOrEmpty(step.url) && Strings.isNullOrEmpty(step.artifactoryUrl) && Strings.isNullOrEmpty(step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = Strings.emptyToNull(Strings.trimEnd(step.url, "/"));
    String artifactoryUrl = Strings.isNullOrEmpty(step.artifactoryUrl) ? (urlWithoutSlash + "/" + "artifactory") : step.artifactoryUrl;
    String distributionUrl = Strings.isNullOrEmpty(step.distributionUrl) ? (urlWithoutSlash + "/" + "distribution") : step.distributionUrl;

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (!Strings.isNullOrEmpty(step.credentialsId)) {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```

The changes include:

* Importing the `com.google.common.base.Strings` class to replace the removed `isAllBlank` method.
* Using `Strings.isNullOrEmpty` instead of `isEmpty` for checking null or empty strings.
* Using `Strings.emptyToNull` instead of `removeEnd` for removing trailing slashes.
* Using `Strings.trimEnd` instead of `defaultIfBlank` for trimming and setting default values.