```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] placeholderByteArray = new byte[0]; // Placeholder as byte array is not available in this context
    long placeholderLong = 0L; // Placeholder as long value is not available in this context
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, placeholderByteArray, placeholderLong);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build(Collections.singleton(mutatedClass)));
  }
```