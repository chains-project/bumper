```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classBytes = null; // replace with actual class bytes
    long classCRC = 0L; // replace with actual CRC
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classCRC);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```