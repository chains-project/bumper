```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder classInfoBuilder = new ClassInfoBuilder();
    byte[] placeholderBytes = new byte[0];
    long placeholderLong = 0L;
    ClassInfo classInfo = classInfoBuilder.getClassInfo(data.getMutatedClass(), placeholderBytes, placeholderLong);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```