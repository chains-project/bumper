Here's the proposed patch to fix the error:

```java
import org.jfrog.artifactory.client.ArtifactoryServer;
import org.jfrog.artifactory.client.distribution.DistributionServer;
import org.jfrog.artifactory.client.impl.ArtifactoryServerImpl;
import org.jfrog.artifactory.client.impl.DistributionServerImpl;
import org.jfrog.hudson.pipeline.scripted.steps.JFrogPlatformInstance;

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
        artifactoryServer = new ArtifactoryServerImpl(artifactoryUrl, step.credentialsId);
        distributionServer = new DistributionServerImpl(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServerImpl(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServerImpl(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```

The changes I made are:

* Importing the missing classes `ArtifactoryServerImpl` and `DistributionServerImpl` from the `org.jfrog.artifactory.client.impl` package.
* Creating instances of `ArtifactoryServer` and `DistributionServer` using their implementation classes `ArtifactoryServerImpl` and `DistributionServerImpl` respectively.

These changes should fix the "cannot find symbol" error.