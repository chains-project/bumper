```java
public void execute() throws Exception {
    if (server == null) {
        throw new IllegalStateException("Artifactory server must be configured");
    }
    if (StringUtils.isAllBlank(kanikoImageFile, jibImageFile) || StringUtils.isNoneBlank(kanikoImageFile, jibImageFile)) {
        throw new IllegalStateException("Exactly one of 'kanikoImageFile' or 'jibImageFile' must be configured");
    }
    CommonDeployer deployer = new CommonDeployer();
    deployer.setServer(server);
    deployer.setRepo(sourceRepo);
    FilePath tempDir = ExtractorUtils.createAndGetTempDir(ws);
    CreateDockerBuildEnvExtractor envExtractor = new CreateDockerBuildEnvExtractor(build, buildInfo, deployer, listener, launcher, tempDir, env, kanikoImageFile, jibImageFile);
    String buildDockerCreator = "org.jfrog.build.extractor.docker.extractor.BuildDockerCreator";
    super.execute("Create Docker Build", buildDockerCreator, envExtractor, tempDir);
}
```