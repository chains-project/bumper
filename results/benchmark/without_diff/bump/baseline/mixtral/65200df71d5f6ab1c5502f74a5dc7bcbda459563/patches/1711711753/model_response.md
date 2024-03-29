Here's a possible patch to fix the error:

```java
private static AnalysisEngineConfiguration buildAnalysisEngineConfiguration() {
    FileWorkingDirProvider workDirProvider = new FileWorkingDirProvider();
