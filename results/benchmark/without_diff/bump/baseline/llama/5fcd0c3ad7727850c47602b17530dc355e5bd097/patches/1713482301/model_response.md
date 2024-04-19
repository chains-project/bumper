Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    List<MutationInfo> mutations = data.getMutations();
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(fileName, mutations, classInfo);
}
```
The error was caused by the fact that the `CoverageDatabase` class has no method `getClassInfo` that takes a single `Class` argument. The patch fixes this by using the `getClassInfo` method that takes a `Collection` of `Class` objects, and passing a `Collections.singleton` collection containing the `MutatedClass` as an argument.

This patch can be applied by replacing the failing code with the above code.