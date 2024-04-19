```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] bytes = new byte[0];
    long timeStamp = System.currentTimeMillis();
    ClassInfoVisitor classInfoVisitor = new ClassInfoVisitor();
    ClassInfoBuilder classInfoBuilder = classInfoVisitor.getClassInfo(mutatedClass, bytes, timeStamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```