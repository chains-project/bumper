```java
public void execute() throws Exception {
    if (server == null) {
        throw new IllegalStateException("Artifactory server must be configured");
    }
    if (StringUtils.isBlank(kanikoImageFile) && StringUtils.isBlank(jibImageFile)) {
        throw new IllegalStateException("At least one of 'kanikoImageFile' or 'jibImageFile' must be configured");
    }
    if (StringUtils.isNotBlank(kanikoImageFile) && StringUtils.isNotBlank(jibImageFile)) {
        throw new IllegalStateException("Only one of 'kanikoImageFile' or 'jibImageFile' should be configured");
    }
    CommonDeployer deployer = new CommonDeployer();
    deployer.setServer(server);
    deployer.setRepo(sourceRepo);
    FilePath tempDir = ExtractorUtils.createAndGetTempDir(ws);
    EnvExtractor envExtractor = new CreateDockerBuildEnvExtractor(build, buildInfo, deployer, listener, launcher, tempDir, env, kanikoImageFile, jibImageFile);
    super.execute("Create Docker Build", "org.jfrog.build.extractor.docker.extractor.BuildDockerCreator", envExtractor, tempDir);
}
```