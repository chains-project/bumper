```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder builder = new ClassInfoVisitor();
    ClassName className = data.getMutatedClass();
    byte[] bytes = new byte[0]; // Replace with appropriate byte array
    long timeStamp = 0L; // Replace with appropriate timestamp
    ClassInfo classInfo = builder.getClassInfo(className, bytes, timeStamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), Collections.singleton(classInfo));
  }
```