import { atom } from 'recoil';

interface ApiState {
    success: any;
    fail: any;
}
const initialState = {
    success: null,
    fail: null,
};

export const duplicatedState = atom<{ id: ApiState, email: ApiState }>({
    key: 'duplicatedState',
    default: {
        id: initialState,
        email: initialState,
    },
});

export const joinState = atom<ApiState>({
    key: 'joinState',
    default: initialState,
});
