```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = getClassBytesFromSomewhere(); // you need to implement this method
    long timestamp = getTimestampFromSomewhere(); // you need to implement this method
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```