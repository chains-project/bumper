```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = data.getMutatedClass();
    final List<ClassName> classes = Collections.singletonList(mutatedClass);
    final byte[] classBytes = coverage.getClassByteCode(mutatedClass);
    final long classTimeStamp = coverage.getClassTimestamp(mutatedClass);
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfoVisitor().getClassInfo(mutatedClass, classBytes, classTimeStamp);
    for (final MutationResult mutationResult : data.getMutations()) {
      classInfoBuilder.visitMethod(mutationResult.getMethod(), mutationResult.getLocation(), mutationResult.getStatus());
    }
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
  }
```