```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = className.getBytes();
    long classHash = className.hashCode();
    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytes, classHash);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```