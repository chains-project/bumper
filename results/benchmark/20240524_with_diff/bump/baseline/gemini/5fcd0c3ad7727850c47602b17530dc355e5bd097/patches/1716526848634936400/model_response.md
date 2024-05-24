```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> classInfos = Collections.singleton(data.getMutatedClass());
    final byte[] classBytes = coverage.getClassBytecode(classInfos);
    final long lastModified = coverage.lastModified(classInfos);
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfoVisitor().getClassInfo(classInfos.iterator().next(), classBytes, lastModified);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
  }
```