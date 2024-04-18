Here is a fixed version of the `run()` method that should resolve the compilation error:

```java
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

The only change I made is to import the missing `isAllBlank` method. It seems that this method is not defined in the code snippet you provided, so I assume it is defined elsewhere in your codebase. You will need to make sure that this method is visible to the `run()` method. If it is defined in the same class, you can simply add the following import statement at the beginning of the file:

```java
import static org.jfrog.hudson.pipeline.scripted.steps.CreateJFrogPlatformInstanceStep.isAllBlank;
```

If it is defined in a different class, you will need to import the entire class or use an appropriate import statement to make the method visible.