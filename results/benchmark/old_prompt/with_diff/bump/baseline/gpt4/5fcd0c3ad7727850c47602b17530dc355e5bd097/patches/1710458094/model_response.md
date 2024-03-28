```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass().iterator().next();
    byte[] byteCode = null; // You need to fetch the byte code for the class
    long timeStamp = 0L; // You need to fetch the timestamp for when the class was modified
    ClassInfoVisitor classInfoVisitor = new ClassInfoVisitor();
    ClassInfoBuilder classInfo = classInfoVisitor.getClassInfo(mutatedClass, byteCode, timeStamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo.build());
  }
```
Please note that you need to fetch the byte code for the class and the timestamp for when the class was modified. The byte code and timestamp arguments are placeholders and need to be replaced with the actual values.