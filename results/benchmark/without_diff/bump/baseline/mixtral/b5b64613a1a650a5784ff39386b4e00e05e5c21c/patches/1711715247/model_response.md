Here's a patch to fix the issue:
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
      Credentials credentials = null;
      if (!isEmpty(step.credentialsId)) {
          credentials = lookUpCredentialsById(step.credentialsId);
      }
      if (credentials == null) {
          artifactoryServer = new ArtifactoryServer(artifactoryUrl, step.username, step.password);
          distributionServer = new DistributionServer(distributionUrl, step.username, step.password);
      } else {
          artifactoryServer = new ArtifactoryServer(artifactoryUrl, credentials);
          distributionServer = new DistributionServer(distributionUrl, credentials);
      }
      artifactoryServer.setPlatformUrl(urlWithoutSlash);
      return new JFrogPlatformInstance(artifactoryServer, distributionServer, step.url, "");
  }
```
The issue is caused by the removal of the `lookUpCredentialsById` method. Instead of looking up the credentials by ID, we can look them up directly when setting the `ArtifactoryServer` and `DistributionServer` instances. We can use the `Credentials` object directly as a parameter for the constructors of `ArtifactoryServer` and `DistributionServer`.

Note: I assumed the existence of a `lookUpCredentialsById` method that returns a `Credentials` object given a credentials ID. You may need to modify the implementation based on the actual method signature.