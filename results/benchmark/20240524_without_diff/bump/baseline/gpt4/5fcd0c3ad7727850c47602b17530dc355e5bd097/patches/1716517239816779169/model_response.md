```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classBytes = new byte[0]; // You might need to get the actual class bytes
    long classLastModified = 0L; // You might need to get the actual last modified time
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classLastModified);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```