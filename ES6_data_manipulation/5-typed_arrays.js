/* eslint-disable */
export default function createInt8TypeArray(length, position, value) {
        if (position >= length || position < 0) {
                throw new Error('Position outside range');
        }

         const buffer = new ArrayBuffer(length);
         const view = new DateView(buffer);

          view.setInt8(position, value);

          return view;
}
