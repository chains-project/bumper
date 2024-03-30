```
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
    if (!isEmpty(step.credentialsId)) {
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

The error message indicates that the symbol 'ArtifactoryServer' cannot be found. This suggests that the class 'ArtifactoryServer' is not in the project's classpath.

To fix this issue, you can add a dependency on the 'org.jfrog:artifactory-java-client' library, which contains the 'ArtifactoryServer' class.

Here's a patch that you can apply to the code to fix the error:

```
<dependencies>
    <dependency>
        <groupId>org.jfrog</groupId>
        <artifactId>artifactory-java-client</artifactId>
        <version>7.2.0</version>
    </dependency>
</dependencies>
```

You can also try using the fully qualified name 'org.jfrog.artifactory.ArtifactoryServer' instead of 'ArtifactoryServer' to refer to the class.
This should allow the code to compile even if the dependency is not added.

Here's the modified code with the fully qualified name:
```
@Override
protected JFrogPlatformInstance run() throws Exception {
    if (isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = removeEnd(step.url, "/");
    String artifactoryUrl = defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    org.jfrog.artifactory.ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    if (!isEmpty(step.credentialsId)) {
        artifactoryServer = new org.jfrog.artifactory.ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new org.jfrog.artifactory.ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```

This should allow the code to compile and run successfully.