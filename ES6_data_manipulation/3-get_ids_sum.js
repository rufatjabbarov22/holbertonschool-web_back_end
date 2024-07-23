/* eslint-disable */
export default function getStudetIdsSum(students) {
        return students.reduce((sum, student) => sum + students.id, 0);
}
