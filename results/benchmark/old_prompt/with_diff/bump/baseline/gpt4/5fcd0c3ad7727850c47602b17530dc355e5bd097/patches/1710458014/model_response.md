```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classInfoBytes = new byte[0]; // You need to get the actual class bytes
    long timestamp = 0L; // You need to get the actual timestamp
    ClassInfoBuilder classInfo = ClassInfoVisitor.getClassInfo(mutatedClass, classInfoBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo.build());
  }
```