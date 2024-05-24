```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = new ClassName(data.getFileName(), data.getMutatedClass());
    final byte[] classBytes = coverage.getBytes(mutatedClass);
    final long checksum = coverage.getChecksum(mutatedClass);
    final ClassInfo classInfo = coverage.getClassInfoVisitor().getClassInfo(mutatedClass, classBytes, checksum);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```