```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classBytes = {}; // You need to provide appropriate byte array.
    long lastModified = 0L; // You need to provide appropriate last modified time.
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, lastModified);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
  }
```