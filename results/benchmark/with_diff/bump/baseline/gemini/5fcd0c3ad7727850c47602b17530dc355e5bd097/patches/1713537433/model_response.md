```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String className = data.getMutatedClass();
    final byte[] classBytes = coverage.getBytes(className);
    final long classModifiedTime = coverage.getLastModifiedTime(className);
    final ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(ClassName.fromString(className), classBytes, classModifiedTime);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```