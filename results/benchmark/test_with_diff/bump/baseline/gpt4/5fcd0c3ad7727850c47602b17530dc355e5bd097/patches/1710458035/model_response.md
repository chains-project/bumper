```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = className.getBytes();
    long timeStamp = className.getTimeStamp();
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(className, classBytes, timeStamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```