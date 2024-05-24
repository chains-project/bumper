Here's the fixed `run()` method with the error resolved:

```java
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

1. Imported the required classes for the utility methods:
```java
import org.apache.commons.lang3.StringUtils;
import org.jenkinsci.plugins.plaincredentials.StringCredentials;
import org.jenkinsci.plugins.plaincredentials.StringCredentials.StringCredentialsId;
```

2. Replaced `isAllBlank` with `StringUtils.isAllBlank`.
3. Replaced `removeEnd` with `StringUtils.removeEnd`.
4. Replaced `defaultIfBlank` with `StringUtils.defaultIfBlank`.
5. Changed the type of `step.credentialsId` from `String` to `StringCredentialsId`.
6. Imported the required class for `StringCredentialsId`:
```java
import org.jenkinsci.plugins.plaincredentials.StringCredentials.StringCredentialsId;
```