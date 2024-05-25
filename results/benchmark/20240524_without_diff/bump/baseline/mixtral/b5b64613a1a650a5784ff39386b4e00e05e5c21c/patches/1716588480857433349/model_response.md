Here's a potential fix for the issue:

```java
import org.jfrog.buildinfo.client.generic.GenericBuildInfoClient;
import org.jfrog.buildinfo.client.generic.GenericBuildInfoClientFactory;
import org.jfrog.hudson.pipeline.common.types.ArtifactoryServer;
import org.jfrog.hudson.pipeline.common.types.DistributionServer;
import org.jfrog.hudson.pipeline.common.utils.BuildInfoClientCreator;
import org.jfrog.hudson.pipeline.common.utils.CredentialsIdUtils;
import org.jfrog.hudson.pipeline.common.utils.StringUtils;
import org.jfrog.hudson.pipeline.scripted.steps.CreateJFrogPlatformInstanceStep;
import org.jfrog.hudson.pipeline.scripted.steps.JFrogPlatformInstance;

@Override
protected JFrogPlatformInstance run() throws Exception {
    if (StringUtils.isAllBlank(step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    String urlWithoutSlash = StringUtils.removeEnd(step.url, "/");
    String artifactoryUrl = StringUtils.defaultIfBlank(step.artifactoryUrl, urlWithoutSlash + "/" + "artifactory");
    String distributionUrl = StringUtils.defaultIfBlank(step.distributionUrl, urlWithoutSlash + "/" + "distribution");

    ArtifactoryServer artifactoryServer;
    DistributionServer distributionServer;
    String credentialsId = step.credentialsId;
    if (StringUtils.isEmpty(credentialsId)) {
        credentialsId = CredentialsIdUtils.getAutomaticCredentialsId();
    }
    if (StringUtils.isNotEmpty(credentialsId)) {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, credentialsId);
        distributionServer = new DistributionServer(distributionUrl, credentialsId);
    } else {
        artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);

    GenericBuildInfoClient buildInfoClient = BuildInfoClientCreator.createBuildInfoClient(artifactoryServer, distributionServer);
    return new JFrogPlatformInstance(artifactoryServer, distributionServer, buildInfoClient, step.url, "");
}
```

The changes made include:

* Importing the necessary classes for the `GenericBuildInfoClient` and `GenericBuildInfoClientFactory`.
* Updating the `if` statements to use `StringUtils` instead of `isEmpty`, `isAllBlank`, and `defaultIfBlank`.
* Adding a `credentialsId` variable to simplify the logic for creating the `ArtifactoryServer` and `DistributionServer` objects.
* Changing the creation of the `ArtifactoryServer` and `DistributionServer` objects to use the `credentialsId` variable.
* Adding a check for automatic credentials if the `credentialsId` is empty.
* Creating a `GenericBuildInfoClient` object to pass to the `JFrogPlatformInstance` constructor.
* Updating the `JFrogPlatformInstance` constructor to accept the `GenericBuildInfoClient` object.

Note: This code assumes that the necessary dependencies have been added to the project. If not, the necessary dependencies will need to be added to the project's build configuration.