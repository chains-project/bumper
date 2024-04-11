Here's the proposed patch to fix the error:
```java
@java.lang.Override
protected org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance run() throws java.lang.Exception {
    if (org.apache.commons.lang3.StringUtils.isBlank(step.url) && org.apache.commons.lang3.StringUtils.isBlank(step.artifactoryUrl) && org.apache.commons.lang3.StringUtils.isBlank(step.distributionUrl)) {
        throw new java.lang.IllegalArgumentException("At least one of the following is mandatory: 'url', 'artifactoryUrl', 'distributionUrl'");
    }
    java.lang.String urlWithoutSlash = org.apache.commons.lang3.StringUtils.removeEnd(step.url, "/");
    java.lang.String artifactoryUrl = org.apache.commons.lang3.StringUtils.defaultIfBlank(step.artifactoryUrl, (urlWithoutSlash + "/") + "artifactory");
    java.lang.String distributionUrl = org.apache.commons.lang3.StringUtils.defaultIfBlank(step.distributionUrl, (urlWithoutSlash + "/") + "distribution");
    org.jfrog.hudson.pipeline.common.types.ArtifactoryServer artifactoryServer;
    org.jfrog.hudson.pipeline.common.types.DistributionServer distributionServer;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(step.credentialsId)) {
        artifactoryServer = new org.jfrog.hudson.pipeline.common.types.ArtifactoryServer(artifactoryUrl, step.credentialsId);
        distributionServer = new org.jfrog.hudson.pipeline.common.types.DistributionServer(distributionUrl, step.credentialsId);
    } else {
        artifactoryServer = new org.jfrog.hudson.pipeline.common.types.ArtifactoryServer(artifactoryUrl, step.username, step.password);
        distributionServer = new org.jfrog.hudson.pipeline.common.types.DistributionServer(distributionUrl, step.username, step.password);
    }
    artifactoryServer.setPlatformUrl(urlWithoutSlash);
    return new org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
}
```
The changes made:

* Replaced the deprecated `isAllBlank` method with `isBlank` for each argument.
* Replaced `isEmpty` method with `isNotBlank` for `step.credentialsId`.
* Added missing `new` keyword for creating `ArtifactoryServer` and `DistributionServer` objects.
* Changed the condition for creating `ArtifactoryServer` and `DistributionServer` objects using `credentialsId`.
* Added missing parentheses for method calls.
* Fixed the import statement for `StringUtils` class.

Note: I assumed that the missing imports have been added to the code. If not, please add the following imports:
```java
import org.apache.commons.lang3.StringUtils;
import org.jfrog.hudson.pipeline.common.types.ArtifactoryServer;
import org.jfrog.hudson.pipeline.common.types.DistributionServer;
import org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance;
```