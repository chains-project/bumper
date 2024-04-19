Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(classInfoBuilder.getClassName()));
}
```
Explanation:

The failing method `createSummaryData` is modified to use the `org.pitest.classinfo.ClassInfoBuilder` class to get the `ClassInfo` object for the mutated class. The `ClassInfoBuilder` class is used to create a `ClassInfo` object from a `ClassName` object, which is obtained from the `ClassMutationResults` object. The `getClassInfo` method of the `CoverageDatabase` class is then called with the `ClassName` object obtained from the `ClassInfoBuilder`, to get the `ClassInfo` object for the mutated class.


The reason for this change is that the `getClassInfo` method of the `CoverageDatabase` class has been removed in the new library version, and the `ClassInfoBuilder` class provides an alternative way to obtain a `ClassInfo` object.