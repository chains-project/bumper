Here is a proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<String> mutatedClass = data.getMutatedClass();
    ClassInfo classInfo = coverage.getClassInfo(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```

In this patch, I created a new variable `mutatedClass` to store the result of `data.getMutatedClass()`, and used it to get the `ClassInfo` object from `coverage`. This way, the code should not rely on any removed library methods.