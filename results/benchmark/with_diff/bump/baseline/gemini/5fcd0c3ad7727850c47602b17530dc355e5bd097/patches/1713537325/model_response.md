```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName className = new ClassName(data.getMutatedClass());
    final byte[] bytecode = coverage.getBytes(className);
    final long time = coverage.getLastModifiedTime(className);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), ClassInfoBuilder.getClassInfo(className, bytecode, time));
  }
```