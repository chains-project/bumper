```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = data.getMutatedClass();
    final byte[] classBytes = null; // Replace with actual class bytes if available
    final long classHash = 0L; // Replace with actual class hash if available
    final ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classHash);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), Collections.singleton(classInfoBuilder.build()));
  }
```