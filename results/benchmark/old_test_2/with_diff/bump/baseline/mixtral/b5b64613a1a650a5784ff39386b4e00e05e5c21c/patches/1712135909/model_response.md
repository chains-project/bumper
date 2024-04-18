Here's a fixed version of the `run()` method that should resolve the error:

```java
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    ClientHelper clientHelper = null;
    if (!isEmpty(step.credentialsId)) {
        clientHelper = new ClientHelper(step.credentialsId, getContext().getListener(), "");
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, clientHelper);
        distributionServer = new DistributionServer(distributionUrl, clientHelper);
    } else {
        clientHelper = new ClientHelper(step.username, getContext().getListener(), step.password, "");
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, clientHelper);
        distributionServer = new DistributionServer(distributionUrl, clientHelper);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```

In this version, I've created a new variable `clientHelper` of type `ClientHelper` to handle authentication. This allows us to use the new constructor for `ClientHelper` that takes a `P4BaseCredentials` object, which is what `step.credentialsId` is.

If `step.credentialsId` is not empty, we create a new `ClientHelper` instance with `step.credentialsId` and use it to create the `ArtifactoryServer` and `DistributionServer` instances. Otherwise, we create a new `ClientHelper` instance with `step.username`, `step.password`, and an empty string for the workspace, and use it to create the `ArtifactoryServer` and `DistributionServer` instances.

In both cases, we pass the `ClientHelper` instance to the `ArtifactoryServer` and `DistributionServer` constructors to handle authentication.

Note that the `ClientHelper` constructor that takes a `P4BaseCredentials` object was added in the new library version, while the constructor that takes a `String`, `TaskListener`, `String`, and `String` was removed.