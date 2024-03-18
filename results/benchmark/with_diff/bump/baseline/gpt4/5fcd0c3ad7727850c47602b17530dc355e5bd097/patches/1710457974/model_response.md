```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass().iterator().next();
    byte[] classBytes = {}; // You need to replace this with actual class bytes
    long timestamp = 0L; // You need to replace this with actual timestamp
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```