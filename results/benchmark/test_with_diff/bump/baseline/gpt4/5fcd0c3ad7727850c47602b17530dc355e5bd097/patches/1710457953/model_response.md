```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass().iterator().next();
    byte[] classBytes = new byte[0]; // You need to get the actual class bytes
    long classDate = 0L; // You need to get the actual class date
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, classDate);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```