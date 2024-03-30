Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())),
        Collections.singletonList(data.getMutatedClass()));
}
```
The patch adds a fourth parameter `Collections.singletonList(data.getMutatedClass())` to the constructor of `MutationTestSummaryData`. This is because the `getClassInfo` method of `CoverageDatabase` has been updated to return a `List` of `ClassInfo` objects, whereas previously it returned a single `ClassInfo` object. By passing a singleton list containing the mutated class, we can adapt the code to the new API.

Note that the method signature remains unchanged, and the patch only modifies the method body.