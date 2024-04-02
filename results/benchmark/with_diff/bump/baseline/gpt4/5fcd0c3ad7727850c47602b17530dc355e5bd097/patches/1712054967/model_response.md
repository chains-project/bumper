```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classData = null; // Replace with actual class data if available
    long timeStamp = 0; // Replace with actual timestamp if available
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(mutatedClass, classData, timeStamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```