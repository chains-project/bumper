Here's the fixed `execute` method. I replaced the usage of `org.apache.commons.lang3.StringUtils.isAllBlank` with a custom method `areBothNullOrBlank` that checks if both `kanikoImageFile` and `jibImageFile` are either null or blank.

This method has the same behavior as `isAllBlank` but it only takes two String arguments, making it compatible with the existing code.

```java
public void execute() throws java.lang.Exception {
    if (server == null) {
        throw new java.lang.IllegalStateException("Artifactory server must be configured");
    }
    if (areBothNullOrBlank(kanikoImageFile, jibImageFile) || !areBothNullOrBlank(kanikoImageFile, jibImageFile)) {
        throw new java.lang.IllegalStateException("Exactly one of 'kanikoImageFile' or 'jibImageFile' must be configured");
    }
    org.jfrog.hudson.pipeline.common.types.deployers.CommonDeployer deployer = new org.jfrog.hudson.pipeline.common.types.deployers.CommonDeployer();
    deployer.setServer(server);
    deployer.setRepo(sourceRepo);
    hudson.FilePath tempDir = org.jfrog.hudson.util.ExtractorUtils.createAndGetTempDir(ws);
    org.jfrog.hudson.pipeline.common.executors.EnvExtractor envExtractor = new org.jfrog.hudson.pipeline.common.executors.CreateDockerBuildEnvExtractor(build, buildInfo, deployer, listener, launcher, tempDir, env, kanikoImageFile, jibImageFile);
    super.execute("Create Docker Build", "org.jfrog.build.extractor.docker.extractor.BuildDockerCreator", envExtractor, tempDir);
}

private boolean areBothNullOrBlank(String str1, String str2) {
    return (str1 == null || str1.isEmpty()) && (str2 == null || str2.isEmpty());
}
```

This patch only changes the `execute` method by adding a new private helper method `areBothNullOrBlank` and using it in the condition.