Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    String className = data.getMutatedClass().getCanonicalName();
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(className));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch removes the `Override` annotation, as it's not necessary, and uses `getCanonicalName()` instead of `getClassName()` to get the canonical name of the mutated class. This should fix the error and allow the code to compile successfully.